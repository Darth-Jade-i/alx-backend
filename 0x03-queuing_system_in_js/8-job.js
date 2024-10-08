import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate through each job in jobs array
  jobs.forEach((jobData) => {
    // Create a new job in the queue 'push_notification_code_3'
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
      });

    // Event when the job is completed
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Event when the job has failed
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Event to track the job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
