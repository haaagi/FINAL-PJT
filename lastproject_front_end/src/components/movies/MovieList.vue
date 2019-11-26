<template>
    <div>
        <h1>MovieList</h1>
     <b-card-group deck>
    <div v-for="movie in movies" :key="movie.id" class="col-3 my-3">
 
    <b-card title="Title" :img-src="movie.poster_url" :img-alt="movie.title" img-top>
      <b-card-text>
        This is a wider card with supporting text below as a natural lead-in to additional content.
        This content is a little bit longer.
      </b-card-text>
    </b-card>
  
</div>
</b-card-group> 



        <!-- <ul>
            <li v-for="movie in movies" :key="movie.id">
                <img :src="movie.poster_url" :alt="movie.title">
                {{ movie.title }}
            </li>
        </ul>   -->
    </div>
</template>


<script>
export default {
    name: 'MovieList',
    data() {
        return {

        }
    },
    props: {
        movies: Array,
    }
}
</script>

<style>
    
</style>