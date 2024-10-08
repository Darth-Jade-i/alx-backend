// Import the Redis library using the ES6 import statement
import redis from 'redis';

// Create a Redis client instance that connects to the Redis server
// running on the default host (127.0.0.1) and port (6379)
const client = redis.createClient();

// Listen for the 'connect' event to know when the
// connection to Redis has been successfully established
client.on('connect', () => {
  // Log a success message when the connection is successful
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event to capture any issues with the Redis connection
client.on('error', (err) => {
  // Log an error message if there is a problem connecting to Redis
  console.log('Redis client not connected to the server:', err.message);
});
