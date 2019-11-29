<template>
  <div class="user-detail">
    <!-- <h1>로그인됨</h1>
    <div>{{ getuserinfo.age }}</div>
    <div>{{ getuserinfo.username }}</div>
    <button>팔로우</button> -->


    <div class="card">
    <div class="content">
      <div class="header">
       <h4>{{ getuserinfo.username }}</h4>
       <p>({{ getuserinfo.kakao_id }})</p>
      </div>
      <div class="meta">
        {{ getuserinfo.age }} | {{ getuserinfo.gender }}
      </div>
      <div class="description">
        
      </div>
    </div>
    <div class="extra content">
      <div class="ui two buttons">
        <div class="ui basic green button">팔로우</div>
        <div class="ui basic red button">팔로우취소</div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
  import {
    mapGetters
  } from 'vuex';
  export default {
    name: 'UserDetail',
    computed: {
      ...mapGetters(['getuserinfo'])
    }
  }
</script>

<style>

</style>