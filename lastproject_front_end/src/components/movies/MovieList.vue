<template>
    <div>
        <h1>MovieList</h1>
        <ul>
            <li v-for="movie in movies" :key="movie.id">
                <img :src="movie.poster_url" :alt="movie.title">
                {{ movie.title }}
            </li>
        </ul>  
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