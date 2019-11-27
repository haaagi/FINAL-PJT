const axios = require('axios');
import router from '../../router';



const state = {
    moviePickList: [],
};

const mutations = {
    



}

const actions = {
    moviePick: (movie_id) => {
        axios.get(`http://localhost:8000/api/movie_detail/${movie_id}`)
            .then(res=> moviePickList.push(res.data))
            .catch(err => console.error(err))
    },
    
};


export default {
    state, getters, mutations, actions
}