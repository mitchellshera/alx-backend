import { createClient } from 'redis';

function redisOperations() {
  const client = createClient();

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

  // Function to display the value for a school in Redis
  function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
      if (err) {
        console.error(`Error getting value for ${schoolName}: ${err}`);
      } else {
        console.log(`Value for ${schoolName}: ${value}`);
      }
    });
  }

  // Gracefully handle process termination
  process.on('SIGINT', () => {
    client.quit();
    process.exit();
  });

  // Call the new functions
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}

// Call the main function to initiate Redis operations
redisOperations();
