<template>
  <div>
    <div class="about">
      <div class="container">
        <div class="container_box p-3">
          <div class="row">
            <div class="col-md-6 xs-12">
              <div class="card__collection clear-fix">
                <div class="cards cards--two">
                  <img
                    src="@/assets/img/about-me.jpg"
                    class="img-responsive"
                    alt="Cards Image"
                  />
                  <span class="cards--two__rect"></span>
                  <span class="cards--two__tri"></span>
                  <p>Mark Anthony Vale</p>
                  <ul class="cards__list">
                    <li>
                      <a
                        href="https://www.facebook.com/markavale"
                        style="color: white"
                        target="new"
                        ><i class="fab fa-facebook-f"></i
                      ></a>
                    </li>
                    <li>
                      <a
                        href="https://github.com/markavale"
                        style="color: white"
                        target="new"
                        ><i class="fab fa-github"></i
                      ></a>
                    </li>
                    <li>
                      <a
                        href="https://www.instagram.com/markavale_/"
                        style="color: white"
                        taret="new"
                        ><i class="fab fa-instagram"></i
                      ></a>
                    </li>
                    <li>
                      <a
                        href="https://www.linkedin.com/in/mark-anthony-vale-b0b169199/"
                        style="color: white"
                        target="new"
                        ><i class="fab fa-linkedin-in"></i
                      ></a>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 90%"
                  aria-valuenow="0"
                  aria-valuemin="10"
                  aria-valuemax="100"
                >
                  HTML, CSS, JS
                </div>
              </div>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 80%"
                  aria-valuenow="75"
                  aria-valuemin="25"
                  aria-valuemax="100"
                >
                  Python
                </div>
              </div>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 50%"
                  aria-valuenow="50"
                  aria-valuemin="0"
                  aria-valuemax="100"
                >
                  Mysql, Postgresql
                </div>
              </div>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 60%"
                  aria-valuenow="75"
                  aria-valuemin="25"
                  aria-valuemax="100"
                >
                  Vue JS
                </div>
              </div>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 70%"
                  aria-valuenow="70"
                  aria-valuemin="30"
                  aria-valuemax="100"
                >
                  Vuetify
                </div>
              </div>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 60%"
                  aria-valuenow="75"
                  aria-valuemin="25"
                  aria-valuemax="100"
                >
                  Bootstrap
                </div>
              </div>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 80%"
                  aria-valuenow="100"
                  aria-valuemin="0"
                  aria-valuemax="100"
                >
                  Django & Django REST Framework
                </div>
              </div>
            </div>
            <div class="col-md-6 xs-12 p-3">
              <!-- <div class="container">
              
              </div> -->
              <v-container>
                <h5 class="title-header">About me</h5>
                <p class="lead">
                  Mark Anthony Vale is a self-employed and actively looking for
                  a Web development position , Mark is fueled by his passion for
                  understanding different tech stacks. He considers himself a
                  "forever student", eager to build on his academic foundation
                  in computer science to stay in tune with the latest
                  technology.
                </p>
                <p class="lead">
                  His hunger for knowledge and determination to turn ideas into
                  action has contributed to a successful thesis project, wherein
                  he led developing a web application called "E-barangay", it
                  aims to improve a local government unit services through
                  descriptive analytics. Also, his thesis groupmates and his
                  thesis adviser wrote three research papers and got accepted
                  for oral presentation.
                </p>
                <p class="lead">
                  Mark believes competing to yourself and not to others is key
                  to success. Mark has interest in music, photography and
                  videography. He also loves to travel and document his travel
                  experiences.
                </p>
              </v-container>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="about__hobby">
      <!-- <div class="container">
        
        </div> -->
      <v-container fluid>
        <div class="row">
          <div class="col-sm-12">
            <h1
              class="title-header center mt-3"
              style="color: #fff; font-size: 3rem; font-weight: 650"
            >
              What I do?
            </h1>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6 col-xs-12 px-2">
            <Timeline />
          </div>
          <div
            class="col-md-6 col-xs-12"
            style="height: 300px"
            id="rotatingCube"
          >
            <div id="wrapper">
              <div class="box-area">
                <div
                  id="box-front"
                  class="box"
                  :style="{ backgroundImage: 'url(' + box.frontImage + ')' }"
                  style="
                    background-size: 425px 425px;
                    background-repeat: no-repeat;
                    background-color: rgba(17, 25, 48, 0.5);
                  "
                ></div>
                <div
                  id="box-right"
                  class="box"
                  :style="{ backgroundImage: 'url(' + box.rightImage + ')' }"
                  style="
                    background-size: 400px 450px;
                    background-repeat: no-repeat;
                    background-color: rgba(17, 25, 48, 0.5);
                  "
                ></div>
                <div
                  id="box-back"
                  class="box"
                  :style="{ backgroundImage: 'url(' + box.backImage + ')' }"
                  style="
                    background-size: 400px 380px;
                    background-repeat: no-repeat;
                    background-color: rgba(17, 25, 48, 0.5);
                  "
                ></div>
                <div
                  id="box-left"
                  class="box"
                  :style="{ backgroundImage: 'url(' + box.leftImage + ')' }"
                  style="
                    background-size: 400px 380px;
                    background-repeat: no-repeat;
                    background-color: rgba(17, 25, 48, 0.5);
                  "
                ></div>
                <div id="box-top" class="box"></div>
                <div id="box-bottom" class="box"></div>
              </div>
            </div>
          </div>
        </div>
      </v-container>
    </div>
  </div>
</template>

<script>
import frontImage from "@/assets/img/webdev-3.png";
import rightImage from "@/assets/img/graphic-design-1.png";
import backImage from "@/assets/img/videography-1.png";
import leftImage from "@/assets/img/photography-1.png";
import Timeline from "@/components/index/Timeline";
export default {
  name: "About",
  data() {
    return {
      box: {
        frontImage,
        rightImage,
        backImage,
        leftImage,
      },
    };
  },
  components: {
    Timeline,
  },
};
</script>

<style scoped lang="css">
*,
*:before,
*:after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.about {
  margin: 70px;
}
/* custom */
.title-header {
  font-size: 2rem;
  position: relative;
  margin-bottom: 16px;
}

.title-header:before {
  content: "";
  position: absolute;
  height: 3px;
  background-color: #0078ff;
  width: 100px;
  bottom: -12px;
}

.progress {
  margin: 15px 0;
  height: 30px;
}
.progress > .progress-bar {
  text-align: left;
  font-size: 15px;
  color: white;
  font-weight: 400;
  background-color: #459dff;
  padding-left: 10px;
}
.about__hobby {
  background-color: #15314b;
  height: 800px;
  width: 100%;
  border-radius: 0 0 85% 85% / 8%;
}
.about_container {
  padding: 2rem 2.5rem;
}
.about_box_container {
  padding: 1.2rem 1.5rem;
}
/* end */

/* story telling */
.hobby {
  color: white;
  list-style-type: none;
  margin: 0px;
  padding: 0px;

  display: -webkit-flex;
  -webkit-flex-direction: column;

  display: inline-flex;
  flex-direction: column;
}
.hobby-line {
  border-bottom: 3px solid white;
  width: 50%;
}
.hobby h1 {
  font-size: 25px;
  font-weight: 700;
  color: white;
}
.hobby > li {
  width: 80%;
}
.hobby .hobby-icon {
  color: white;
  font-size: 30px;
  font-weight: 500;
  margin: 0;
  padding: 0;
}
.hobby .hobby-icon > .ion-code-working {
  text-align: center;
  margin: 0;
  padding: 0;
}
/* end */

/* portfolio 3D box */
#wrapper {
  /* margin-top:50px; */
  position: absolute;
  left: 50%;
  top: 50%;
  perspective: 1500px;
}
#wrapper2 {
  position: absolute;
  right: 25%;
  top: 50%;
  perspective: 1500px;
}

.box-area {
  position: relative;
  transform-style: preserve-3d;
  animation-name: rotate;
  animation-duration: 30s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  margin: 0;
  padding: 0;
}

@keyframes rotate {
  0% {
    transform: rotate3d(0, 0, 0, 0);
  }
  100% {
    transform: rotate3d(0, 1, 0, 360deg);
  }
}

.box {
  position: absolute;
  width: 400px;
  height: 400px;
  border: 2px solid #262626;
  -webkit-box-shadow: 0 8px 6px -6px black;
  -moz-box-shadow: 0 8px 6px -6px black;
  box-shadow: 0 32px 24px -24px rgba(68, 68, 68, 0.7);
  margin-top: 20px;
  padding: 200px;
}

.box-logo {
  height: 400px;
  width: 400px;
  position: absolute;
}
.img-svg {
  height: 400px;
  width: 400px;
  top: 50%;
  left: 25%;
}

#box-front {
  transform: translateX(-200px) translateY(-100px) translateZ(200px);
  /* background: rgba(255, 16, 107, 0.5); */
  background-color: rgba(17, 25, 48, 0.5);
}

#box-back {
  transform: translateX(-200px) translateY(-100px) translateZ(-200px);
  /* background: rgba(92, 245, 235, 0.5); */
  background: rgba(2, 32, 60, 0.5);
}

#box-right {
  transform: translateY(-100px) rotateY(90deg);
  /* background: rgba(4, 255, 116, 0.5); */
  background: rgba(2, 32, 60, 0.5);
}

#box-left {
  transform: translateY(-100px) translateX(-400px) rotateY(90deg);
  /* background: rgba(216, 255, 0, 0.5); */
  background: rgba(2, 32, 60, 0.5);
}

#box-top {
  transform: translateX(-200px) translateY(-300px) rotateX(90deg);
  /* background: rgba(0, 6, 246, 0.5); */
  background: rgba(25, 41, 56, 0.5);
}

#box-bottom {
  transform: translateX(-200px) translateY(100px) rotateX(90deg);
  /* background: rgba(255, 30, 0, 0.5); */
  background: rgba(25, 41, 56, 0.5);
}

.box-area {
  transform: rotateX(90deg) rotateY(90deg);
}

.shadow {
  -moz-box-shadow: 3px 3px 5px 6px #ccc;
  -webkit-box-shadow: 3px 3px 5px 6px #ccc;
  box-shadow: 3px 3px 5px 6px #ccc;
}
/* End */

.clear-fix:after {
  display: block;
  clear: both;
  content: "";
}

.img-responsive {
  max-width: 100%;
  height: auto;
}

.card__collection {
  position: relative;
  display: block;
  /* background: rgba(10, 10, 10, 0.5); */
  /* padding: 10px; */
  padding: 10px 70px;
  /* font-family: 'Monsteratt'; */
  overflow: hidden;
  /* height:100%; */
}
.card__collection .cards {
  width: 300px;
  height: 400px;
  display: block;
  background-size: cover;
  float: center;
  border-radius: 15px;
  position: relative;
  overflow: hidden;
  background-position: center;
  margin: 10px;
  /* padding:0 auto; */
}
.card__collection .cards--one {
  backface-visiblility: hidden;
}
.card__collection .cards--one:hover:after {
  bottom: -20px;
}
.card__collection .cards--one:hover:before {
  bottom: -10px;
}
.card__collection .cards--one:hover .cards--one__rect {
  left: 45%;
}
.card__collection .cards--one:hover .cards--one__rect--back {
  left: 50%;
}
.card__collection .cards--one::after {
  content: "";
  display: block;
  position: absolute;
  height: 70px;
  transform: rotate(-3deg);
  background: #e660e3;
  position: absolute;
  bottom: -80px;
  left: 0;
  right: -10px;
  z-index: 9;
  transition: all 0.2s ease-in;
  transition-delay: 0.3s;
}
.card__collection .cards--one:before {
  content: "";
  display: block;
  position: absolute;
  height: 80px;
  transform: rotate(-3deg);
  bottom: -90px;
  left: 0;
  background: #fff;
  right: -10px;
  z-index: 5;
  transition: all 0.2s ease-in;
  transition-delay: 0.1s;
}
.card__collection .cards--one__rect {
  color: #fff;
  text-transform: uppercase;
  font-size: 18px;
  background: #0f9bc0;
  width: 126px;
  height: 55px;
  transform: skewY(5deg);
  position: absolute;
  display: block;
  top: 60%;
  left: -45%;
  z-index: 1;
  line-height: 3.3rem;
  text-align: center;
  transition: all 0.2s ease-in;
}
.card__collection .cards--one__rect--back {
  display: block;
  background: rgba(34, 65, 154, 0.8);
  width: 126px;
  height: 55px;
  transform: skewY(7deg);
  position: absolute;
  top: 65%;
  left: -50%;
  transition: all 0.2s ease-in;
  transition-delay: 0.3s;
}
.card__collection .cards--one__rect p {
  transform: skewY(-7deg);
  position: relative;
}
.card__collection .cards--two {
  position: relative;
  backface-visibility: hidden;
}
.card__collection .cards--two p {
  position: absolute;
  top: 83%;
  left: -100%;
  text-transform: capitalize;
  color: #fff;
  font-size: 20px;
  z-index: 8;
  transition: all 0.6s ease;
}
.card__collection .cards--two:hover p {
  left: 8%;
}
.card__collection .cards--two:hover img {
  transform: translateY(-15px);
}
.card__collection .cards--two:hover .cards--two__rect {
  top: 75%;
}
.card__collection .cards--two:hover .cards--two__rect:before {
  transform: translateY(15px);
}
.card__collection .cards--two:hover li {
  transform: translateY(0);
}
.card__collection .cards--two:hover .cards--two__tri {
  right: -40%;
}
.card__collection .cards--two:hover .cards--two__tri:before {
  right: -312px;
}
.card__collection .cards--two img {
  transition: all 0.2s ease;
}
.card__collection .cards--two__tri {
  border-top: 220px solid transparent;
  border-bottom: 190px solid transparent;
  border-right: 288px solid #fff;
  opacity: 0.9;
  position: absolute;
  display: block;
  top: 0;
  right: -100%;
  transition: all 0.3s ease-in-out;
}
.card__collection .cards--two__tri:before {
  border-top: 220px solid transparent;
  border-bottom: 190px solid transparent;
  border-right: 288px solid #57ccfd;
  position: absolute;
  content: "";
  display: block;
  top: -220px;
  right: -612px;
  transition: all 0.3s ease-in-out;
  transition-delay: 0.2s;
}
.card__collection .cards--two__rect {
  width: 750px;
  height: 200px;
  background: #fff;
  display: block;
  position: absolute;
  top: 175%;
  left: -78%;
  transform: rotate(30deg);
  z-index: 5;
  opacity: 0.9;
  transition: all 0.3s ease-in-out;
}
.card__collection .cards--two__rect:before {
  content: "";
  display: block;
  width: 100%;
  position: relative;
  height: 100%;
  background: #15314b;
  transform: translateY(200px);
  z-index: 2;
  transition: all 0.3s ease-in-out;
  transition-delay: 0.1s;
}
.card__collection .cards--two ul {
  list-style: none;
  position: absolute;
  bottom: 0;
  left: 10px;
  z-index: 9;
}
.card__collection .cards--two ul li {
  display: inline-block;
  font-size: 16px;
  margin: 7px;
  color: #fff;
  transition: all 0.2s ease-in-out;
  transform: translateY(100px);
}
.card__collection .cards--two ul li:nth-child(2) {
  transition-delay: 0.2s;
}
.card__collection .cards--two ul li:nth-child(3) {
  transition-delay: 0.3s;
}
.card__collection .cards--two ul li:nth-child(4) {
  transition-delay: 0.4s;
}
.card__collection .cards--three {
  position: relative;
  z-index: 10;
}
.card__collection .cards--three:hover .cards--three__rect-1 {
  left: 10%;
}
.card__collection .cards--three:hover .cards--three__rect-1 .shadow-1 {
  left: -20%;
}
.card__collection .cards--three:hover .cards--three__rect-2 {
  left: 60%;
}
.card__collection .cards--three:hover .cards--three__rect-2:before {
  left: -100%;
}
.card__collection .cards--three:hover .cards--three__rect-2:after {
  left: 80%;
}
.card__collection .cards--three:hover .cards--three__rect-2 .shadow-2 {
  left: -10%;
}
.card__collection .cards--three:hover .cards--three__circle {
  transform: scale(1);
}
.card__collection .cards--three:hover .cards--three__circle:before {
  transform: scale(0.9);
}
.card__collection .cards--three:hover .cards--three__list li {
  transform: translateX(0);
}
.card__collection .cards--three__rect-1 {
  background: #fff;
  width: 200px;
  height: 110px;
  transform: skewX(-20deg);
  display: block;
  position: absolute;
  top: 73%;
  opacity: 0.9;
  left: -100%;
  z-index: 8;
  transition: all 0.5s ease-in;
}
.card__collection .cards--three__rect-1 p {
  font-size: 20px;
  color: #fff;
  transform: skewX(20deg);
  line-height: 6rem;
}
.card__collection .cards--three__rect-1 .shadow-1 {
  background: #9b1308;
  width: 230px;
  height: 100px;
  display: block;
  position: absolute;
  left: -200%;
  z-index: -1;
  transition: all 0.3s ease-in;
}
.card__collection .cards--three__rect-2 {
  width: 100px;
  height: 70px;
  background: #fff;
  position: absolute;
  top: 65%;
  left: 1000%;
  opacity: 0.9;
  transform: skewX(-20deg);
  z-index: 8;
  transition: all 0.5s ease-in;
}
.card__collection .cards--three__rect-2::before {
  content: "";
  display: block;
  width: 50px;
  height: 40px;
  background: #57ccfd;
  opacity: 1;
  position: absolute;
  left: 500%;
  top: 10%;
  transition: all 0.3s ease-in;
}
.card__collection .cards--three__rect-2::after {
  content: "";
  display: block;
  width: 50px;
  height: 40px;
  background: #9b1308;
  opacity: 1;
  position: absolute;
  left: 500%;
  top: 114%;
  transition: all 0.5s ease-in;
  transition-delay: 0.2s;
}
.card__collection .cards--three__rect-2 .shadow-2 {
  background: #57ccfd;
  width: 100%;
  height: 100%;
  display: block;
  position: absolute;
  top: -10%;
  left: 500%;
  transition: all 0.5s ease-in;
  transition-delay: 0.2s;
}
.card__collection .cards--three__circle {
  width: 220px;
  height: 220px;
  border-radius: 50%;
  background: #fff;
  position: absolute;
  top: -15%;
  left: 50%;
  opacity: 0.9;
  transform: scale(0);
  transition: all 0.3s ease;
}
.card__collection .cards--three__circle:before {
  content: "";
  display: block;
  width: 100%;
  height: 100%;
  background: #9b1308;
  border-radius: 50%;
  transform: scale(0);
  transition: all 0.3s ease;
  transition-delay: 0.2s;
}
.card__collection .cards--three__list {
  list-style: none;
  position: absolute;
  top: -9px;
  right: 7px;
  padding-top: 60px;
  transition: all 0.4s ease;
}
.card__collection .cards--three__list li {
  display: inline-block;
  margin: 4px;
  color: #fff;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background: rgba(87, 204, 253, 0.9);
  text-align: center;
  line-height: 1.7rem;
  font-size: 12px;
  transition: all 0.3s ease;
  transform: translateX(500%);
}
.card__collection .cards--three__list li:nth-child(1) {
  transition-delay: 0.2s;
}
.card__collection .cards--three__list li:nth-child(2) {
  transition-delay: 0.3s;
}
.card__collection .cards--three__list li:nth-child(3) {
  transition-delay: 0.4s;
}

/* card flipper */
.wrapper {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}

.card-flip {
  width: 420px;
  height: 340px;
  margin: 1em;
  perspective: 1500px;
}
.card-flip .content {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.8s cubic-bezier(0.75, 0, 0.85, 1);
}

.more {
  display: none;
}
.more:checked ~ .content {
  transform: rotateY(180deg);
}

.front,
.back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  transform-style: preserve-3d;
  border-radius: 6px;
}
.front .inner,
.back .inner {
  height: 100%;
  display: grid;
  padding: 1.5em;
  transform: translateZ(80px) scale(0.94);
}
.inner > .info span {
  font-size: 25px;
}
.front {
  background-color: #fff;
  background-size: cover;
  background-position: center center;
}
.front:after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 6px;
  backface-visibility: hidden;
  /* background: linear-gradient(40deg, rgba(67, 138, 243, 0.7), rgba(255, 242, 166, 0.7)); */
  background: linear-gradient(
    40deg,
    rgba(21, 49, 75, 0.7),
    rgba(0, 120, 255, 0.7)
  );
}
.front .inner {
  grid-template-rows: 5fr 1fr 1fr 2fr 1fr;
  justify-items: center;
}
.front h2 {
  grid-row: 2;
  margin-bottom: 0.3em;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: #fff;
  font-weight: 500;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.1);
}
.front .rating {
  grid-row: 3;
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
  display: flex;
  flex-flow: row nowrap;
}
.front .rating i {
  margin: 0 1px;
}

.back {
  transform: rotateY(180deg);
  background-color: #fff;
  border: 2px solid #f0f0f0;
}
.back .inner {
  grid-template-rows: 1fr 2fr 1fr 2fr 14fr 1fr 1fr;
  grid-template-columns: repeat(4, auto);
  grid-column-gap: 0.8em;
  justify-items: center;
}
.back .info {
  position: relative;
  display: flex;
  align-items: center;
  color: #355cc9;
  grid-row: 3;
}
.back .info:not(:first-of-type):before {
  content: "";
  position: absolute;
  left: -0.9em;
  height: 18px;
  width: 1px;
  background-color: #ccc;
}
.back .info span {
  font-size: 2em;
  font-weight: 700;
}
.back .info i {
  font-size: 1.2em;
}
.back .info i:before {
  background: linear-gradient(40deg, #355cc9, #438af3);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}
.back .info .icon {
  margin-left: 0.3em;
}
.back .info .icon span {
  display: block;
  margin-top: -0.25em;
  font-size: 0.8em;
  font-weight: 600;
  white-space: nowrap;
}
.back .description {
  grid-row: 5;
  grid-column: 1/-1;
  font-size: 1em;
  border-radius: 5px;
  font-weight: 600;
  line-height: 1.4em;
  overflow: auto;
  color: #355cc9;
  padding-right: 10px;
}
.back .location,
.back .price {
  font-weight: 600;
  color: #355cc9;
  grid-row: 1;
  font-size: 0.86em;
}
.back .location {
  grid-column: 1/3;
  justify-self: left;
}
.back .price {
  grid-column: 3/-1;
  justify-self: right;
}
.back .button {
  grid-column: 1/-1;
  justify-self: center;
}

.button {
  grid-row: -1;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  cursor: pointer;
  display: block;
  padding: 0 1.5em;
  height: 3em;
  line-height: 2.9em;
  min-width: 3em;
  background-color: transparent;
  border: solid 2px #fff;
  color: #fff;
  border-radius: 4px;
  text-align: center;
  left: 50%;
  backface-visibility: hidden;
  transition: 0.3s ease-in-out;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
}
.button:hover {
  background-color: #fff;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);
  text-shadow: none;
  color: #355cc9;
}
.button.return {
  line-height: 3em;
  color: #355cc9;
  border-color: #355cc9;
  text-shadow: none;
}
.button.return:hover {
  background-color: #355cc9;
  color: #fff;
  box-shadow: none;
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #859ddf;
}

::-webkit-scrollbar-thumb:hover {
  background: #355cc9;
}

/* simple card flip */
.portfolio-icons > a {
  color: #15314b;
  font-size: 20px;
  font-weight: 500;
}
.card-simple-flip {
  width: 300px;
  height: 250px;
  background: #000;
  border-radius: 1rem;
  margin: 10px auto;
}
.card-simple-flip .image-card {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-color: #0078ff;
}
.card-simple-flip .image-card img {
  width: 150px;
  transition: 0.5s;
  height: 150px;
  margin: 50px 0;
}
.card-simple-flip:hover .image-card img {
  opacity: 0.5;
  transform: translateX(30%); /*100%*/
}
.card-simple-flip .details {
  position: absolute;
  top: 0;
  left: 0;
  width: 70%; /*100%*/
  height: 100%;
  background: #ffc107;
  transition: 0.5s;
  transform-origin: left;
  transform: perspective(2000px) rotateY(-90deg);
}
.card-simple-flip:hover .details {
  transform: perspective(2000px) rotateY(0deg);
}
.card-simple-flip .details .center {
  padding: 20px;
  text-align: center;
  background: #fff;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.card-simple-flip .details .center h1 {
  margin: 0;
  padding: 0;
  color: #15314b;
  line-height: 20px;
  font-size: 20px;
  text-transform: uppercase;
}
.card-simple-flip .details .center h1 span {
  font-size: 14px;
  color: #262626;
}
.card-simple-flip .details .center p {
  margin: 10px 0;
  padding: 0;
  color: #262626;
}
.card-simple-flip .details .center ul {
  margin: 10px auto 0;
  padding: 0;
  display: table;
}
.card-simple-flip .details .center ul li {
  list-style: none;
  margin: 0 5px;
  float: left;
}
.card-simple-flip .details .center ul li a {
  display: block;
  background: #262626;
  color: #fff;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  transform: 0.5s;
}
.card-simple-flip .details .center ul li a:hover {
  background: #ff3636;
}
/* end */
@media screen and (min-width: 767px) and (max-width: 950px) {
  #rotatingCube {
    display: none;
  }
}
@media screen and (min-width: 300px) and (max-width: 767px) {
  .about_container {
    padding: 1rem 1.5rem;
  }
  .card__collection {
    padding: 10px;
    margin-right: 5px;
  }
  .img-responsive {
    margin: 0 auto;
  }
  #wrapper {
    display: none;
  }
  ul.hobby {
    text-align: center;
    padding: 0;
    margin: 0 0 20px 0;
  }
  .hobby > li {
    text-align: center;
    margin: 0 auto;
  }
  .hobby-line {
    margin: 0 auto;
  }
}
@media screen and (max-width: 992px) {
  .about {
    margin: 35px;
  }
  .about_container {
    padding: 1.5rem;
  }
}

/* On screens that are 600px or less, set the background color to olive */
@media screen and (max-width: 600px) {
  .about {
    margin: 20px;
  }
  .about_container {
    padding: 1.3rem 2rem;
  }
  .about_box_container {
    padding: 5px;
  }
}
</style>