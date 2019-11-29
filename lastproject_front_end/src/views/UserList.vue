<template>
  <div>
    <!-- <div v-for="user in users" :key="user.id">
        <div class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-secondary">{{user.username}}</button>
            <button @click="follow(user.id)" type="button" class="btn btn-secondary">팔로우</button>
            <button @click="follow(user.id)" type="button" class="btn btn-secondary">언팔</button>
        </div>
    </div> -->
      <ul class=list-group list-group-horizontal v-for="user in users" :key="user.id">
        <li class="list-group-item"> {{ user.username }}</li>
        <div class="list-group-item">
            <button @click="follow(user.id)" class="ui basic green button">팔로우</button>
        </div>
        <div class="list-group-item">
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