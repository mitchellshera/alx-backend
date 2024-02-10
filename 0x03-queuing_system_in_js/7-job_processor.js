import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    job.log(`Phone number ${phoneNumber} is blacklisted`);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Gracefully handle process termination
process.on('SIGINT', () => {
  queue.shutdown(5000, (err) => {
    console.log('Job processor has been shut down.');
    process.exit(err ? 1 : 0);
  });
});
