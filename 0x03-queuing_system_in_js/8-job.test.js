import { expect } from 'chai';
import { describe, it, before, after, afterEach } from 'mocha';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  // Before running tests, enter test mode
  before(() => {
    queue.testMode.enter();
  });

  // After running tests, exit test mode
  after(() => {
    queue.testMode.exit();
  });

  // Clear the queue after each test
  afterEach(() => {
    queue.testMode.clear();
  });

  it('should display an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(5, queue)).to.throw(Error, 'Jobs is not an array');
  });

  // it('should create two new jobs to the queue', () => {
  //   const jobs = [
  //     {
  //       phoneNumber: '4153518780',
  //       message: 'This is the code 1234 to verify your account'
  //     },
  //     {
  //       phoneNumber: '4153518781',
  //       message: 'This is the code 4321 to verify your account'
  //     }
  //   ];

  //   createPushNotificationsJobs(jobs, queue);

  //   // Check that two jobs were created
  //   expect(queue.testMode.jobs.length).to.equal(2);

  //   // Check that the job type is correct
  //   expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  //   expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');

  //   // Check the data inside the jobs
  //   expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
  //   expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  // });

  it('display a error message if jobs is not an array passing Number', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
    // expect(queue.testMode.job[0]);
  });

  it('display a error message if jobs is not an array passing Object', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
    // expect(queue.testMode.job[0]);
  });

  it('display a error message if jobs is not an array passing String', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
    // expect(queue.testMode.job[0]);
  });

  it('should NOT display a error message if jobs is an array with empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
    // expect(queue.testMode.job[0]);
  });

  it('should NOT display a error message if jobs is an array with empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
    // expect(queue.testMode.job[0]);
  });

  // it('create two new jobs to the queue', () => {
  //   const jobs = [
  //     {
  //       phoneNumber: '4153518780',
  //       message: 'This is the code 1234 to verify your account',
  //     },
  //     {
  //       phoneNumber: '4153118782',
  //       message: 'This is the code 4321 to verify your account',
  //     },
  //   ];
  //   createPushNotificationsJobs(jobs, queue);
  //   expect(queue.testMode.jobs.length).to.equal(2);

  //   expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');

  //   expect(queue.testMode.jobs[0].data).to.eql({
  //     phoneNumber: '4153518780',
  //     message: 'This is the code 1234 to verify your account',
  //   });

  //   expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');

  //   expect(queue.testMode.jobs[1].data).to.eql({
  //     phoneNumber: '4153118782',
  //     message: 'This is the code 4321 to verify your account',
  //   });
  // });
});
