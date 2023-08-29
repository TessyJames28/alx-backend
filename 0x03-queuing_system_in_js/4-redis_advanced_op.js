import redis from 'redis';
const client = redis.createClient();

client.on('error', err => {
  console.error('Redis client not connected to the server:', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});


client.hset('HolbertonSchools', 'Portland', 50, (err, val) => {
  redis.print(`Reply: ${val}`);
});

client.hset('HolbertonSchools', 'Seattle', 80, (err, val) => {  
  redis.print(`Reply: ${val}`);
});

client.hset('HolbertonSchools', 'New York', 20, (err, val) => { 
  redis.print(`Reply: ${val}`);
});

client.hset('HolbertonSchools', 'Bogota', 20, (err, val) => { 
  redis.print(`Reply: ${val}`);
});

client.hset('HolbertonSchools', 'Cali', 40, (err, val) => { 
  redis.print(`Reply: ${val}`);
});

client.hset('HolbertonSchools', 'Paris', 2, (err, val) => { 
  redis.print(`Reply: ${val}`);
});

client.hgetall('HolbertonSchools', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
