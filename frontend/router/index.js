import Vue from 'vue';
import VueRouter from 'vue-router';
import NoteList from '../components/NoteList.vue';
import NoteDetail from '../components/NoteDetail.vue';
import NoteForm from '../components/NoteForm.vue';
import SearchResults from '../components/SearchResults.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/notes',
        name: 'NoteList',
        component: NoteList,
    },
    {
        path: '/notes/:id',
        name: 'NoteDetail',
        component: NoteDetail,
    },
    {
        path: '/notes/create',
        name: 'NoteForm',
        component: NoteForm,
    },
    {
        path: '/notes/:id/edit',
        name: 'NoteForm',
        component: NoteForm,
    },
    {
        path: '/search',
        name: 'SearchResults',
        component: SearchResults,
    },
    {
        path: '/',
        redirect: '/notes',
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
