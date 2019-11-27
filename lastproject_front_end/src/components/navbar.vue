<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="info">
      <router-link to="/"><b-navbar-brand href="#">Home</b-navbar-brand></router-link> 
    

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
              
              <router-link to="/userdetail"><b-dropdown-item href="#">userdetail</b-dropdown-item></router-link>
              
              <router-link to="/userlist"><b-dropdown-item href="#">User List</b-dropdown-item></router-link>
              <b-dropdown-item href="#" @click.prevent="logout">Log Out</b-dropdown-item>

            </div>
            <div v-else>
              
               <router-link to="/login"> <b-dropdown-item>Login</b-dropdown-item></router-link>
               <router-link to="/signup"><b-dropdown-item>sign-up </b-dropdown-item></router-link>
              
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