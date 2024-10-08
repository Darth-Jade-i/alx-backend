// Import the Redis library
import redis from 'redis';

// Create a Redis client instance
const client = redis.createClient();

// Listen for the 'connect' event to log a successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event in case of connection failure
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

/**
 * Store a hash in Redis with the key 'HolbertonSchools' and multiple fields.
 */
function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

/**
 * Retrieve and log the entire hash 'HolbertonSchools' from Redis.
 */
function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(err);  // Log any errors
    } else {
      console.log(reply);  // Log the entire hash object
    }
  });
}

// Call the function to create and display the hash
createHash();
displayHash();
