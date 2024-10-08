import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();
const queue = kue.createQueue();
const getAsync = promisify(client.get).bind(client);

let availableSeats = 50;
let reservationEnabled = true;

client.set('available_seats', availableSeats);

// Get current available seats
const getCurrentAvailableSeats = async () => {
    const seats = await getAsync('available_seats');
    return seats ? parseInt(seats) : 0;
};

// Route for available seats
app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (!err) {
            res.json({ status: 'Reservation in process' });
        } else {
            res.json({ status: 'Reservation failed' });
        }
    });
});

// Route to process queue
app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const seats = await getCurrentAvailableSeats();

        if (seats <= 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }

        client.decr('available_seats');
        const updatedSeats = await getCurrentAvailableSeats();
        if (updatedSeats === 0) reservationEnabled = false;

        done();
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
