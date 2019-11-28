<template>
<div class="modal fade" tabindex="-1" role="dialog" :id="`movie-${movie.id}`">

  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header" style="text-align: center">

        <h5 class="modal-title">{{ movie.title }}</h5>
        <p>({{movie.title_eng}})</p>
        
        <button @click="likeMovie(movie.id)"><i class="heart icon"></i></button>
        <button><i class="heart outline icon"></i></button>

        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">

        <img class="movie--poster my-3 imgess" :src="movie.poster_url" :alt="movie.name">
        
        <div class="container icon-des">
          <p><i class="calendar alternate icon"></i>개봉일 {{movie.open_date}}</p>  
          <p><i class="user alternate icon"></i> 관객수 {{movie.audience}}</p>  
          <p><i class="eye alternate icon"></i> 관람등급 {{movie.watch_grade}}</p>

          <p><i class="star alternate icon"></i> 평점 {{movie.user_rating}}</p>


        </div>
        <hr>

        <p>{{ movie.description }}</p>
        <p><a :href="movie.naver_link">...더보기</a></p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>


</template>

<script>

const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios'); 

  export default {
    name: 'MovieListItemModal',
    props: {
      movie: Object,
    },
    data () {
      return {
        // clickedMovie: 0,
      }
    },

    methods: {
      // clickLike(movie) {
      //   this.clickedMovie = movie;
      // },
      likeMovie (movie_id) {
            const hash = sessionStorage.getItem('jwt');
            const options = {
            headers: {
                Authorization:'JWT ' + hash
            }
        }
            axios.get(HOST + 'api/movielike/'+ movie_id + '/', options)           
            .then(res=> console.log(res))
            .catch(err => console.error(err))
            
        }

    },
    

  }
</script>

<style>
#modal-title {
   text-align: center;

}
#imgess {
  float: left;
  margin-right: 20px;
  margin-top: 20px;
  clear: both;
}
</style>