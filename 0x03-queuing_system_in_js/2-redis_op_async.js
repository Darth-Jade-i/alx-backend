// Import the Redis library and util to promisify functions
import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client instance
const client = redis.createClient();

// Listen for the 'connect' event to log when the client connects successfully
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event in case of connection failure
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Promisify the `get` method from the Redis client to use async/await
const getAsync = promisify(client.get).bind(client);

/**
 * setNewSchool - This function stores a key-value pair in Redis.
 * @param {string} schoolName - The key representing the school name.
 * @param {string} value - The value to be stored for the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);  // Log an error if it occurs
    } else {
      console.log(reply);  // Log the Redis confirmation message ('OK')
    }
  });
}

/**
 * displaySchoolValue - Asynchronously retrieves the value for a given key from Redis.
 * @param {string} schoolName - The key representing the school name to be retrieved.
 */
async function displaySchoolValue(schoolName) {
  try {
    // Await the result of the promisified get method
    const value = await getAsync(schoolName);
    console.log(value);  // Log the value retrieved from Redis
  } catch (err) {
    console.error(err);  // Log any errors that occur during retrieval
  }
}

// Call the function to display the value for 'Holberton'
displaySchoolValue('Holberton');

// Set a new school value in Redis and then display it
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
