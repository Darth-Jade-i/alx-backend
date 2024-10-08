// Import the Redis library
import redis from 'redis';

// Create a Redis client instance
const subscriber = redis.createClient();

// Listen for the 'connect' event
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event
subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Subscribe to the 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(`${message}`);
  
  // If the message is 'KILL_SERVER', unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
