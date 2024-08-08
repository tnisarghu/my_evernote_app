import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        searchQuery: '',
    },
    mutations: {
        setSearchQuery(state, query) {
            state.searchQuery = query;
        }
    },
    actions: {
        searchNotes({ commit }, query) {
            commit('setSearchQuery', query);
        }
    },
    modules: {
    }
});
