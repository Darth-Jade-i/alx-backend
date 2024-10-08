// Import the kue library to create a queue
const kue = require('kue');

// Create a queue instance for managing jobs
const queue = kue.createQueue();

// Define the function that sends the notification
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs from the queue named 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
  // Extract phone number and message from the job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message);

  // Mark the job as done once the notification is sent
  done();
});
