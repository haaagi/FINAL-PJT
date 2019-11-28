<template>
  <div>
      <ul v-for="user in users" :key="user.id">
        <li> {{ user.username }}</li>
        <div v-if="!flag">
            <button @click="follow(user.id)" class="ui basic green button">팔로우</button>
        </div>
        <div v-else>
            <button @click="follow(user.id)" class="ui basic green button">팔로우 취소</button>
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
            flag:0,

        }
    },
    methods: {
        follow (star_id) {
            this.flag = !this.flag
            const hash = sessionStorage.getItem('jwt');
            const options = {
            headers: {
                Authorization:'JWT ' + hash
            }
        }
            axios.get(HOST + 'api/accounts/userfollow/'+star_id + '/', options)
            .then(res=> {
                console.log(res)
                this.resdata = res.data
            })
            .catch(err => console.error(err))
            
        }

    },
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