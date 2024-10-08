// Import the Redis library to interact with the Redis server
import redis from 'redis';

// Create a Redis client instance
// that connects to the Redis server
const client = redis.createClient();

// Listen for the 'connect' event to know
// when the connection to Redis is successful
client.on('connect', () => {
  // Log a message when the Redis client
  // connects to the server successfully
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event in case
// there is an issue connecting to Redis
client.on('error', (err) => {
  // Log the error message if Redis fails to connect
  console.log('Redis client not connected to the server:', err.message);
});

/**
 * setNewSchool - This function stores
 * a key-value pair in the Redis database.
 * @param {string} schoolName - The key representing the school name.
 * @param {string} value - The value to be
 * associated with the key (schoolName).
 */
function setNewSchool(schoolName, value) {
  // Use the Redis client to set the value
  // for the specified key (schoolName)
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);  // If an error occurs, log the error
    } else {
      // Log the confirmation message from Redis
      // after successfully setting the value
      console.log(reply);  // Output 'OK' indicating success
    }
  });
}

/**
 * displaySchoolValue - This function retrieves the
 * value associated with a given key from Redis.
 * @param {string} schoolName - The key representing
 * the school name whose value is to be retrieved.
 */
function displaySchoolValue(schoolName) {
  // Use the Redis client to get the value
  // for the specified key (schoolName)
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);  // If an error occurs, log the error
    } else {
      // Log the value associated with the key to the console
      // Output the value, or null if the key does not exist
      console.log(reply);
    }
  });
}

// Call the function to display the value
// of the key 'Holberton' from Redis
displaySchoolValue('Holberton');

// Call the function to set the value '100'
// for the key 'HolbertonSanFrancisco'
setNewSchool('HolbertonSanFrancisco', '100');

// Call the function to display the value of
// the key 'HolbertonSanFrancisco' from Redis
displaySchoolValue('HolbertonSanFrancisco');
