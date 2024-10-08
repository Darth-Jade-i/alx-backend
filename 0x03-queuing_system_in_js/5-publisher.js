// Import the Redis library
import redis from 'redis';

// Create a Redis client instance
const publisher = redis.createClient();

// Listen for the 'connect' event
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event
publisher.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

/**
 * publishMessage - Publishes a message to the channel after a delay.
 * @param {string} message - The message to be published.
 * @param {number} time - The delay in milliseconds before publishing the message.
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

// Publish messages with varying delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
