<template>
<div>
  <span v-if="isLoggedIn">
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="">Logout</a>
        <router-link to="/userdetail">userdetail</router-link>
        <router-link to="/userlist">userlist</router-link>
      </span>
      
      <span v-else>
        <div>
          <router-link to="/login">Login</router-link>
        </div>
        <div>
          <router-link to="/signup">sign-up</router-link>
        </div>
    </span>

  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">
      <router-link to="/">Home</router-link> |
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
            <div v-if="isLoggedIn">
              <b-dropdown-item href="http://localhost:8080/userdetail">
              </b-dropdown-item>
              <b-dropdown-item href="#">User List</b-dropdown-item>
              <b-dropdown-item href="#" @click.prevent="logout">Log Out</b-dropdown-item>

            </div>
            <div v-else>
               <b-dropdown-item href="http://localhost:8080/login">Log In</b-dropdown-item>
               <b-dropdown-item href="http://localhost:8080/signup">Sign Up</b-dropdown-item>
            </div>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>


</template>

<script>
import { mapActions, mapGetters } from 'vuex';
  export default {
    name: 'navbar',
    methods: {
    ...mapActions(['login', 'logout']),
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
  }, 
  
  }
</script>

<style>

</style>