<template>
  <div>
      <ul v-for="user in users" :key="user.id">
          <li> {{ user.age }}</li>
          <div>
                   <div class="ui two buttons">
        <div class="ui basic green button" >팔로우</div>

      </div>

          </div>
      </ul>
  </div>
</template>

<script>
const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios'); 
export default {
    name: 'UserList',
    data () {
        return {
            users: [],
        }
    },
    method: {
        // nothing (star_id) {
            // axios.get

        },

    // },
    created () {
        const hash = sessionStorage.getItem('jwt');
        const options = {
        headers: {
            Authorization:'JWT ' + hash
        }
    }
        axios.post(HOST + 'api/accounts/userlist/',null , options)
        .then(res=> this.users = res.data)
    }
}
</script>

<style>

</style>