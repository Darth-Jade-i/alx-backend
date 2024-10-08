// Import the kue library to create a queue
const kue = require('kue');

// Create a queue instance for managing jobs
const queue = kue.createQueue();

// Array of job data for multiple notifications
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153518741', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518742', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153518741', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518742', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153518741', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518742', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153518741', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518742', message: 'This is the code 4321 to verify your account' },
  // Add more job data as required
];

// Iterate over each job in the array
jobs.forEach((jobData) => {
  // Create a new job in the queue named 'push_notification_code_2'
  const job = queue.create('push_notification_code_2', jobData)
    .save((err) => {
      // Log the job ID if saved successfully
      if (!err) console.log(`Notification job created: ${job.id}`);
    });

  // Event listener for job completion
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Event listener for job failure
  job.on('failed', (errorMessage) => {
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });

  // Event listener for job progress
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
