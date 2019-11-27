<template>
  <div>
      <ul v-for="user in users" :key="user.id">
          <li> {{ user.age }}</li>
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
        axios.post('http://localhost:8000/api/accounts/userinfo/',null , options)
        .then(res=> this.users = res.data)
    }
}
</script>

<style>

</style>