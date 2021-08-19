<template>
  <div class="">
    <DashboardLayout>
      <template slot="content">
        <section class="tab border-b-2 mt-10 border-gray-200">
        </section>
        <section class="dashboard-table mt-16 pb-10">
          <div class="pl-10 pr-20">
            <section class="w-full pb-5 text-left">
              <div class="p-8">
                <div class="grid grid-cols-2 gap-5">
                  <div class="text-left">
                    <label class="text-sm block mb-3 text-gray-400">Name</label>
                    <input
                      type="text"
                      placeholder="Name"
                      v-model="tweetData.name"
                      class="border rounded-md py-2 px-2 w-full border-gray-200"
                    >
                  </div>
                  <div class="text-left">
                    <label class="text-sm block mb-3 text-gray-400">Tweet</label>
                    <input
                      type="text"
                      placeholder="Tweet"
                      v-model="tweetData.tweet"
                      class="border rounded-md py-2 px-2 w-full border-gray-200"
                    >
                  </div>
                  <div class="text-left">
                    <button
                      class="rounded-lg gig-button px-5 hover justify-center items-center py-3"
                      @click="addTweet"
                    >
                      <span class="text-white text-sm">Tweet</span>
                    </button>
                  </div>
                </div>
              </div>
            </section>
          </div>
          <div class="pl-10 pr-20">
            <section class="w-full pb-5">
              <table class="admin-custom-table1">
                <thead>
                  <tr class="font-bold text-gray-500 text-sm">
                    <th>#</th>
                    <th>
                      <a
                        href="javascript:;"
                        class="flex justify-center items-center hover"
                        @click="sort('name')"
                      >
                        <span>Name</span>
                        <img src="../assets/images/svgs/Group 288.svg" class="w-5 ml-2">
                      </a>
                    </th>
                    <th>Message</th>

                    <th>
                      <a
                        href="javascript:;"
                        class="flex justify-center items-center hover"
                        @click="sort('date')"

                      >
                        <span>Time</span>
                        <img src="../assets/images/svgs/Group 288.svg" class="w-5 ml-2">
                      </a>
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-show="tweets.length <= 0">
                    <td colspan="4">
                      <p class="text-center">No tweets found...</p>
                    </td>
                  </tr>
                  <tr v-if="loading">
                    <td colspan="4">
                      <p class="text-center">Loading, please wait...</p>
                    </td>
                  </tr>
                  <tr
                    class="text-gray-400 text-sm center-text"
                    v-for="(tweet, index) in tweets"
                    :key="index"
                    v-else
                  >
                    <td>{{ ++index }}</td>
                    <td>{{ tweet.name }}</td>
                    <td>{{ tweet.tweet }}</td>
                    <td>{{ formatDate(tweet.date_created) }}</td>
                  </tr>
                </tbody>
              </table>
            </section>
          </div>

        </section>
      </template>
    </DashboardLayout>
  </div>
</template>

<script>
// @ is an alias to /src
import DashboardLayout from '@/components/DashboardLayout.vue';

export default {
  name: 'Home',
  components: {
    DashboardLayout,
  },
  data() {
    return {
      loading: true,
      tweetData: {
        name: '',
        tweet: '',
      },
      tweets: [],
    };
  },
  mounted() {
    this.getTweets();
  },
  methods: {
    onCancel() {},
    addTweet() {
      this.startLoadingScreen();
      this.$http.post('tweet/', this.tweetData)
        .then((res) => {
          this.stopLoadingScreen();
          this.getTweets();
          this.tweetData.name = '';
          this.tweetData.tweet = '';
          this.$toast(res.data.message ?? 'Tweet successfully added!', { type: 'success' });
        })
        .catch(() => {
          this.stopLoadingScreen();
          this.$toast('An Error has occurred!', { type: 'error' });
        });
    },
    getTweets() {
      this.startLoadingScreen();
      this.$http.get('tweet/')
        .then((res) => {
          this.stopLoadingScreen();
          this.tweets = res.data;
        })
        .catch(() => {
          this.stopLoadingScreen();
          this.$toast('An error occurred', { type: 'error' });
        });
    },
    sort(field) {
      this.$http.get(`tweet?sort=${field}`)
        .then((res) => {
          this.stopLoadingScreen();
          this.tweets = res.data;
          this.$toast('Data sorted successfully', { type: 'success' });
        })
        .catch(() => {
          this.stopLoadingScreen();
          this.$toast('An error occurred', { type: 'error' });
        });
    },
    startLoadingScreen() {
      this.$nprogress.start();
      this.loading = true;
    },
    stopLoadingScreen() {
      this.$nprogress.done();
      this.loading = false;
    },
  },
};
</script>
