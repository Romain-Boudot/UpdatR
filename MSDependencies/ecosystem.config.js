module.exports = {
  apps : [{
    name: 'CheckDependencies',
    cmd: 'DependenciesChecker.py',
    interpreter: 'python3',
    autorestart: false,
    watch: true,
    pid: '/path/to/pid/file.pid',
    instances: 4,
    max_memory_restart: '1G',
    env: {
      ENV: 'development'
    },
    env_production : {
      ENV: 'production'
    }
  }]
};
