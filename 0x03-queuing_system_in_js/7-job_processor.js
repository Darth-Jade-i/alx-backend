// Import the kue library to create a queue
const kue = require('kue');

// Create a queue instance for managing jobs
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Define the function to send notifications and track job progress
const sendNotification = (phoneNumber, message, job, done) => {
  // Initial progress set to 0
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Update progress to 50% before sending the notification
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Mark the job as done
  done();
};

// Process jobs from the queue 'push_notification_code_2', handling two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
