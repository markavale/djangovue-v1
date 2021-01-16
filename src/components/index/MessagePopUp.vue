<template>
  <div>
    <transition name="slide-fade">
      <div class="greetings" v-if="show">
        <v-card color="#23305e" dark width="350px" elevation="20">
          <div class="">
            <div class="float-right ma-2">
              <v-btn
                fab
                dark
                x-small
                color="error"
                @click.prevent="closeMessage"
              >
                <v-icon dark> mdi-close-thick </v-icon>
              </v-btn>
            </div>
            <v-card-title class="mb-0 pb-0">
              <div class="row">
                <div class="col-xs-2">
                  <img
                    class="rounded-circle article-img"
                    src="@/assets/img/pop-img.jpg"
                  />
                </div>
                <div class="col-xs-10">
                  <h2 class="article-name">Mark Anthony Vale</h2>
                  <span
                    class="font-weight-normal article-sub ml-2 mt-0 pt-0"
                    style="color: white; font-size: 16px"
                    >Developer</span
                  >
                </div>
              </div>
            </v-card-title>
            <v-card-title class="headline mb-2">
              <TextTyping :txtMessages="hello" />
            </v-card-title>

            <v-card-subtitle class="font-weight-normal body-1"
              >I hope all is well with you and your family. Stay safe and stay
              positive. All is well ✌ <br />God bless you.</v-card-subtitle
            >
          </div>
        </v-card>
      </div>
    </transition>
    <transition name="slide-fade">
      <div class="rateCard" v-if="showRate">
        <v-card
          class="elevation-16 mx-auto"
          dark
          color="#23305e"
          width="350"
          :disabled="loading"
          elevation="20"
        >
          <v-progress-linear
            :active="loading"
            :indeterminate="loading"
            height="5"
          ></v-progress-linear>
          <v-card-title class="headline"> Rate My Website </v-card-title>
          <v-card-text class="white--text pb-0">
            If you enjoy staying here, please take a few seconds to rate with my
            website. It really helps!
            <div class="text-center my-3">
              <v-rating
                v-model="rating"
                color="yellow"
                background-color="grey"
                empty-icon="$ratingFull"
                half-increments
                hover
                large
              ></v-rating>
            </div>
            <v-textarea
              name="input-7-4"
              v-model="comment"
              rows="3"
              row-height="25"
              label="Leave a comment (Optional) "
              hint="By clicking rate now, you consent that you are willing rate this website."
              outlined
              class="mb-0"
            ></v-textarea>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions class="justify-space-between">
            <v-btn text @click="noThanks"> No Thanks </v-btn>
            <v-btn text @click="rateNow"> Rate Now </v-btn>
          </v-card-actions>
        </v-card>
      </div>
    </transition>
  </div>
</template>

<script>
import TextTyping from "@/components/index/TextTyping";
export default {
  name: "message-pop-up",
  //   props:{
  //       show:boolean,
  //   },
  data() {
    return {
      hello: [
        "Kamusta!",
        "Hello!",
        "Konnichiwa!",
        "Anyoung!",
        "Nǐ hǎo!",
        "Hola!",
        "Bonjour!",
        "Olá!",
        "Goedendag!",
        "Yassas!",
        "Halo!",
        "Selam!",
        "Hej, Tjena!",
        "Hei!",
      ],
      show: false,
      showRate: false,
      survey: false,
      avatar: "@/assets/img/pop-img.jpg",
      rating: 4,
      comment: "",
      loading: false,
      errors: [],
    };
  },
  components: {
    TextTyping,
  },
  mounted() {
    this.popUpMessage();
  },
  methods: {
    showRateSurvery() {
      setTimeout(() => {
        this.showRate = true;
      }, 2000);
    },
    popUpMessage() {
      setTimeout(() => {
        this.show = true;
        setTimeout(() => {
          this.show = false
          this.showRateSurvery();
        }, 10000);
      }, 7000);
    },
    closeMessage() {
      this.show = false;
      // console.log("Cookie value: " + this.getCookie("survey"));
      if (this.getCookie("survey") == null) {
        // console.log("Cookie not use ");
        this.showRateSurvery();
      } else {
        // console.log("Cookie in use");
        this.showRate = false;
      }
    },
    surveyCookie(key, value) {
      var date = new Date();
      // Default at 365 days.
      var days = 40; // || 365;
      // Get unix milliseconds at current time plus number of days
      date.setTime(+date + days * 86400000); //24 * 60 * 60 * 1000
      window.document.cookie =
        key + "=" + value + "; expires=" + date.toGMTString() + "; path=/";

      // console.log(document.cookie);
      return value;
    },
    getCookie(name) {
      // Split cookie string and get all individual name=value pairs in an array
      var cookieArr = document.cookie.split(";");

      // Loop through the array elements
      for (var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");

        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if (name == cookiePair[0].trim()) {
          // Decode the cookie value and return
          return decodeURIComponent(cookiePair[1]);
        }
      }
      // Return null if not found
      return null;
    },
    oneDaySurveyCookie(key, value) {
      var date = new Date();
      // Default at 365 days.
      var days = 1; // || 365;
      // Get unix milliseconds at current time plus number of days
      date.setTime(+date + days * 86400000); //24 * 60 * 60 * 1000
      window.document.cookie =
        key + "=" + value + "; expires=" + date.toGMTString() + "; path=/";

      // console.log(document.cookie);
      return value;
    },
    noThanks() {
      this.showRate = false;
      this.$store.dispatch('skipUser')
      this.oneDaySurveyCookie("survey", true);
    },
    rateNow() {
      this.loading = true;
      this.survey = true;
      this.$store
        .dispatch("addRating", {
          rate: this.rating,
          comment: this.comment,
        })
        .then(() => {
          this.surveyCookie("survey", true);
          this.showRate = false;
          this.$toast.success({
            title: "Rate Success",
            message: `You rated ${this.rating} stars. Thank you for your time rating my website.`,
            type: "success",
            position: "top right",
            icon: require("../../assets/icons/check-circle-white.png"),
            closeButton: true,
            timeOut: 5000,
            showDuration: 500,
            hideDuration: 500,
            showMethod: "fadeIn",
            hideMethod: "fadeOut",
            color: "#51A351",
          });
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
          let error_data = err.response.data;
          // console.log(error_data);
          for (const field_error in error_data) {
            this.errors.push(error_data[field_error][0]);
          }
        });
    },
  },
};
</script>

<style>
.rateCard {
  position: fixed;
  z-index: 10;
  /* bottom: 80px;
  right: 15px; */
  bottom: 80px;
  left: 15px;
}
.greetings {
  position: fixed;
  z-index: 10;
  bottom: 80px;
  right: 15px;
  /* bottom: 50%;
  right: 15px; */
}
div.message {
  position: fixed;
  z-index: 2;
  height: 350px;
  width: 350px;
  background-color: #23305e;
}
.test-card {
  background-color: #23305e;
}
.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}
.position_greet {
  /* position: fixed; */
  z-index: 5;
  bottom: 25px;
  right: 15px;
  /* width: 50%; */
  width: 350px;
  height: 350px;
  background: #23305e;
}
.message-pop-up {
  position: fixed;
  z-index: 5;
  /* bottom: 15%; */
  bottom: 25px;
  /* margin:0px 0px 10px 0px; */
  right: 15px;
  width: 350px;
  height: auto;
  border: 2px solid #192938;
  border-radius: 0.2in;
  background: #23305e;
  -webkit-box-shadow: 0px 23px 65px -17px rgba(89, 89, 89, 1);
  -moz-box-shadow: 0px 23px 65px -17px rgba(89, 89, 89, 1);
  box-shadow: 0px 23px 65px -17px rgba(89, 89, 89, 1);
}
img.article-img {
  height: 50px;
  width: 50px;
  margin-left: 10px;
}
h2.article-name {
  /* color:#339966; */
  color: #ffffff;
  margin-left: 5px;
  font-size: 20px;
  padding-bottom: 0px;
  margin-bottom: 0px;
}
h2.article-title {
  color: #ffffff;
  padding: 0;
  margin: 0;
  display: inline;
  font-size: 30px;
}
.close-message {
  display: block;
  float: right;
  width: 30px;
  height: 29px;
  color: #ffffff;
  background: red;
  border: 2px solid #eeeeee;
  border-radius: 50%;
  margin: 5px;
}
.close-message:hover {
  transform: scale(1.2, 1.2);
}
.typed-cursor {
  color: #ffffff;
  font-size: 30px;
}
a.article-sub {
  margin-left: 5px;
  color: #ffffff;
  font-style: italic;
  text-decoration: underline;
}
a.article-sub:hover {
  color: #4caf50;
}
p.article-content {
  padding: 5px 0px;
  color: #d4d7e0;
}
.lr-message {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1px;
  color: #339966;
}

.text-slider-items {
  display: block;
}
</style>