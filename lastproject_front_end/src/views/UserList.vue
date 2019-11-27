<template>
  <div>
      <ul v-for="user in users" :key="user.id">
          <li> {{ user.username }}</li>
      </ul>
  </div>
</template>

<script>
const axios = require('axios'); 
export default {
    name: 'UserList',
    data () {
        return {
            users: [],
        }
    },
    created () {
        const hash = sessionStorage.getItem('jwt');
        const options = {
        headers: {
            Authorization:'JWT ' + hash
        }
    }
        axios.get('http://localhost:8000/api/accounts/' , options)
        .then(res=> this.users = res.data)
        .catch(err => console.error(err))
    }
}
</script>

<style>

</style>