<template>
  <div>
      <ul v-for="user in users" :key="user.id">
          <li> {{ user.age }}</li>
          <div>
                   <div class="ui two buttons">
        <div class="ui basic green button">팔로우</div>
        <div class="ui basic red button">팔로우취소</div>
      </div>

          </div>
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
        axios.post('http://localhost:8000/api/accounts/userlist/',null , options)
        .then(res=> this.users = res.data)
    }
}
</script>

<style>

</style>