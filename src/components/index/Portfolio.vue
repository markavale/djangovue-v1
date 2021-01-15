<template>
  <div>
    <div class="portfolio">
      <div class="container">
        <h1>Portfolio</h1>
        <!-- <div class="line-mf"></div> -->
        <div class="row">
          <div class="col-xs-12 col-md-4">
            <div class="card-simple-flip">
              <div class="image-card" style="background-color: #d2b55c">
                <img src="@/assets/img/logo.png" />
              </div>
              <div class="details" style="background-color: #d2b55c">
                <div class="center">
                  <h1>MAV SHOP<br /><span>Developer</span></h1>
                  <p>
                    My own ecommerce web application for selling lightroom
                    presets and photoshop templates.
                  </p>
                  <div class="portfolio-icons">
                    <a href="https://github.com/markavale/mavshopv2/" target="new"
                      ><span><i class="fab fa-github"></i></span
                    ></a>
                    <a href="#under-development" target="new"
                      ><span><i class="fa fa-globe"></i></span
                    ></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xs-12 col-md-4">
            <div class="card-simple-flip">
              <div class="image-card">
                <img src="@/assets/img/ebarangay.png" />
              </div>
              <div class="details" style="background-color: #0078ff">
                <div class="center">
                  <h1>E-Barangay<br /><span>Lead Developer</span></h1>
                  <p>
                    E-barangay a web application for improving local government
                    units through descriptive analytics.
                  </p>
                  <div class="portfolio-icons">
                    <a
                      href="https://github.com/markavale/E-Barangay-v.1.1"
                      target="new"
                      ><span><i class="fab fa-github"></i></span
                    ></a>
                    <a href="http://ebarangay.herokuapp.com/" target="new"
                      ><span><i class="fa fa-globe"></i></span
                    ></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xs-12 col-md-4">
            <div class="card-simple-flip">
              <div class="image-card" style="background-color: #64c89b">
                <img src="@/assets/img/logo.png" />
              </div>
              <div class="details" style="background-color: #64c89b">
                <div class="center">
                  <h1>Covid Tracker<br /><span>Developer</span></h1>
                  <p>
                    A web applicaton for tracking covid cases in Philippines.
                  </p>
                  <div class="portfolio-icons">
                    <a href="https://github.com/markavale/" target="new"
                      ><span><i class="fab fa-github"></i></span
                    ></a>
                    <a
                      href="http://markavale.herokuapp.com/covid-tracker/"
                      target="new"
                      ><span><i class="fa fa-globe"></i></span
                    ></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xs-12 col-md-4">
            <div class="card-simple-flip">
              <div class="image-card" style="background-color: #fe6965">
                <img src="@/assets/img/logo.png" />
              </div>
              <div class="details" style="background-color: #fe6965">
                <div class="center">
                  <h1>Weather API<br /><span>Developer</span></h1>
                  <p>
                    A Weather API web application for fetching data on
                    OpenweatherAPI.
                  </p>
                  <div class="portfolio-icons">
                    <a
                      href="https://github.com/markavale/Weather-App"
                      target="new"
                      ><span><i class="fab fa-github"></i></span
                    ></a>
                    <a
                      href="http://projectweatherapi.herokuapp.com/"
                      target="new"
                      ><span><i class="fa fa-globe"></i></span
                    ></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- <div class="col-xs-12 col-md-4">
        <div class="card-simple-flip">
          <div class="image-card" style="background-color:#c6f559;">
            <img src="{% static 'img/ebarangay.png' %}"/>
          </div>
          <div class="details" style="background-color:#c6f559;">
            <div class="center">
              <h1>E-Barangay<br><span>Lead Developer</span></h1>
              <p>E-barangay a web application for improving local government units through descriptive analytics.</p>
              <div class="portfolio-icons">
                <a href="https://github.com/markavale/Weather-App" target="new"><span><i
                  class="ion-social-github"></i></span></a>
                  <a href="http://projectweatherapi.herokuapp.com/" target="new"><span><i
                    class="fa fa-globe"></i></span></a>
              </div>
            </div>
          </div>
        </div>
      </div>  -->
          <div class="col-xs-12 col-md-4">
            <div class="card-simple-flip">
              <div class="image-card" style="background-color: #536070">
                <img src="@/assets/img/logo.png" />
              </div>
              <div class="details" style="background-color: #536070">
                <div class="center">
                  <h1>Personal Website<br /><span>Developer</span></h1>
                  <p>My own personal website.</p>
                  <div class="portfolio-icons">
                    <a
                      href="https://github.com/markavale/djangovue-v1"
                      target="new"
                      ><span><i class="fab fa-github"></i></span
                    ></a>
                    <a href="http://markanthonyvale.herokuapp.com/" target="new"
                      ><span><i class="fa fa-globe"></i></span
                    ></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.portfolio {
  background-color: #15314b;
  height: auto;
  width: 100%;
  margin: 50px 0 15px 0;
  text-align: center;
  padding: 30px 0;
}
.portfolio > .container > h1 {
  color: white;
  font-size:3rem; 
  font-weight:650;
  text-align: center;
  margin: 0 0 30px 0;
}

.portfolio > .container > h1:before {
  ccontent: "";
  position: absolute;
  height: 3px;
  background-color: #0078ff;
  width: 100px;
  bottom: -12px;
}

div.portfolio-icons > a{
  color:#15314b;
  font-size:20px;
  font-weight: 500;
  margin:2.5px;
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
</style>