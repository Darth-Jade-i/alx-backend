// Import the kue library to create a queue
const kue = require('kue');

// Create a queue instance for managing jobs
const queue = kue.createQueue();

// Define the job data (phone number and message)
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

// Create a job in the queue named 'push_notification_code'
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    // When the job is saved without error, log the job creation message
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

// Event listener for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
