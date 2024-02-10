import { createClient } from 'redis';

function redisAdvancedOperations() {
  const client = createClient();

  client.on('connect', function() {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });

  // Function to create a hash using hset
  function createHash() {
    client.hset('HolbertonSchools', 'Portland', 50, redis.print);
    client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    client.hset('HolbertonSchools', 'New York', 20, redis.print);
    client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    client.hset('HolbertonSchools', 'Paris', 2, redis.print);
  }

  // Function to display the hash using hgetall
  function displayHash() {
    client.hgetall('HolbertonSchools', (err, reply) => {
      if (err) {
        console.error(`Error getting hash values: ${err}`);
      } else {
        console.log(reply);
      }
    });
  }

  // Gracefully handle process termination
  process.on('SIGINT', () => {
    client.quit();
    process.exit();
  });

  // Call the functions
  createHash();
  displayHash();
}

// Call the main function to initiate Redis advanced operations
redisAdvancedOperations();
