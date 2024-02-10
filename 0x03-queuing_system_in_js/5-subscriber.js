import { createClient } from 'redis';

const subscriberClient = createClient();

subscriberClient.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel
subscriberClient.subscribe('holberton school channel');

// Handle incoming messages
subscriberClient.on('message', (channel, message) => {
  console.log(`Received message on channel ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit on KILL_SERVER message
    subscriberClient.unsubscribe('holberton school channel');
    subscriberClient.quit();
  }
});

// Gracefully handle process termination
process.on('SIGINT', () => {
  subscriberClient.unsubscribe('holberton school channel');
  subscriberClient.quit();
  process.exit();
});
