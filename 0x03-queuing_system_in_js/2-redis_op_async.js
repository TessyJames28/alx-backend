import redis from 'redis';
const client = redis.createClient();
import promisify from 'util';

const promisifiedGet = promisify(client.get).bind(client);

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

async function displaySchoolValue(schoolName) {
  const val = promisifiedGet(schoolName);
  console.log(val);
}

export default {
  setNewSchool,
  displaySchoolValue
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
