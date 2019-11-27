<template>
  <div :id="`movie-${movie.id}`">
    <div>
    <h1>movie detail 나와라 ㅠㅠㅠ </h1>
  <b-card no-body class="overflow-hidden" style="max-width: 540px;">
    <b-row no-gutters>
      <b-col md="6">
        <b-card-img :src="movie.poster_url" :alt="movie.title" class="rounded-0"></b-card-img>
      </b-col>
      <b-col md="6">
        <b-card-body>
          <b-card-text>
           <h3><strong>{{ movie.title }}</strong></h3> 
            <span><h4>({{ movie.title_eng }})</h4></span>
            <div>
              {{ movie._genre1 }} | {{ movie._genre2 }} | {{ movie._genre3 }}
            </div>
            <div>
              {{ movie.watch_grade }}
            </div>
            <div>
              {{ movie.description }}
              <a :href="movie.naver_link">...더보기</a>
            </div>

          </b-card-text>
        </b-card-body>
      </b-col>
    </b-row>
    
  </b-card>
</div>
  </div>
</template>

<script>
  export default {
    name: 'MovieDetail',
    props: {
      movie: Object,
    }, 
    // data() {
    //   return {
    //     selectedMovie: Object,
    //   }
    // },
    // methods: {
    //   selectGenre(movie) {
    //     this.selectedMovie = this.movie;
    //   }
    // },



  }
</script>

<style>

</style>