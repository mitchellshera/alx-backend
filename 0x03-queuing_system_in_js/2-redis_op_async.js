import { createClient } from 'redis';
import { promisify } from 'util';

function redisOperationsAsync() {
  const client = createClient();
  const getAsync = promisify(client.get).bind(client);

  client.on('connect', function() {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });

  // Function to set a new school value in Redis
  function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
      if (err) {
        console.error(`Error setting value for ${schoolName}: ${err}`);
      } else {
        console.log(`Value for ${schoolName} set successfully. Reply: ${reply}`);
      }
    });
  }

  // Async function to display the value for a school in Redis
  async function displaySchoolValueAsync(schoolName) {
    try {
      const value = await getAsync(schoolName);
      console.log(`Value for ${schoolName}: ${value}`);
    } catch (err) {
      console.error(`Error getting value for ${schoolName}: ${err}`);
    }
  }

  // Gracefully handle process termination
  process.on('SIGINT', () => {
    client.quit();
    process.exit();
  });

  // Call the new functions
  displaySchoolValueAsync('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValueAsync('HolbertonSanFrancisco');
}

// Call the main function to initiate Redis operations
redisOperationsAsync();
