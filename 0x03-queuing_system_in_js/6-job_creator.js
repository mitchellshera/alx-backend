import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Object containing Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message.',
};

// Create a job and add it to the queue
const notificationJob = queue.create('push_notification_code', jobData);

// On successful job creation
notificationJob.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${notificationJob.id}`);
  } else {
    console.error(`Error creating notification job: ${err}`);
  }
});

// On job completion
notificationJob.on('complete', () => {
  console.log('Notification job completed');
  process.exit(0);
});

// On job failure
notificationJob.on('failed', (err) => {
  console.error(`Notification job failed: ${err}`);
  process.exit(1);
});
