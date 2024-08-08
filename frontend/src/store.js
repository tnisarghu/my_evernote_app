// src/store.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    // ... your store configuration ...
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
