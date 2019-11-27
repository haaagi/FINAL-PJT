<template>
  <div id="app">
    <div id="nav">
    <Navbar />
      <!-- <span v-if="isLoggedIn">
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="">Logout</a> | 
        <router-link to="/userdetail">userdetail</router-link> |
        <router-link to="/userlist">userlist</router-link>
      </span>
      
      <span v-else>
        <div>
          <router-link to="/login">로그인</router-link>
        </div>
        <div>
          <router-link to="/signup">sign-up</router-link>
        </div>
      </span> -->

    </div>
    
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar';
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'App',
  components: {
    Navbar,
  },
  methods: {
    ...mapActions(['login', 'logout']),
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
  }, 
  
}
</script>

<style>
/* 
  1. 컴포넌트마다 비슷한/같은 함수들을 정의 해야함 + 정리가 안됨.
  2. 사용자 auth 정보 & todos 목록을 컴포넌트끼리 공유하지 못함.

  Vuex(State Management System)
 */
 #nav {
  padding-top: 20px;
}
</style>
