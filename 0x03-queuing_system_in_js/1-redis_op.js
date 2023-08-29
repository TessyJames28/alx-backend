import redis from 'redis';
const client = redis.createClient();

client.on('error', err => {
  console.error('Redis client not connected to the server:', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, val) => {
    redis.print(`Reply: ${val}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, val) => {
    if (err) {
      console.error(err);
    } else {
      console.log(val);
    }
  });
}

export default {
  setNewSchool,
  displaySchoolValue
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
