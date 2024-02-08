import { createClient } from 'redis';

function redisConnect() {
  const client = createClient();

  client.on('connect', function() {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });

  // Gracefully handle process termination
  process.on('SIGINT', () => {
    client.quit();
    process.exit();
  });
}

// Call the function to initiate the connection
redisConnect();
