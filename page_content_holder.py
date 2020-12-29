top = """
<!DOCTYPE html>
<html>
<head>


     <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="style/main.css">



        <title> SC Election 2020 </title>


</head>
<body>
    <header class="site-header">
  <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top css-dhro7d-w navpad ">
    <div class="container" id="div.container">
      <a class="navbar-brand mr-4 home_title" href="index.html">
      2020 SC Election
      </a>

      <div class="collapse navbar-collapse css-h6is44" id="navbarToggle" navbar-nav-left>
        <div class="navbar-nav mr-auto dropdown">
          <a class="nav-item nav-link css-193va6t1" href="Candidates_content.html"> House Candidates</a>
          <a class="nav-item nav-link css-193va6t1" href="houseresults.html"> House Results</a>
          <a class="nav-item nav-link css-193va6t1" href="senate_candidates.html"> Senate Candidates</a>
          <a class="nav-item nav-link css-193va6t1" href="senateresults.html"> Senate Results</a>
          <a class="nav-item nav-link css-193va6t1" href="myrep.html"> My Rep?</a>
        <!--     <a class="nav-item nav-link css-193va6t2" href="hack.html">Community</a> -->

        </div>


        <!-- Navbar Right Side -->
        <div class="navbar-nav" whitespace="no-wrap" navbar-nav-right>

                <a class="nav-item nav-link css-193va6t2" href="labs.html">Labs</a>
                <a class="nav-item nav-link css-193va6t1" href="https://projects.fivethirtyeight.com/2020-election-forecast/" target="_blank" rel="noreferrer noopener">Polls</a>
                <a class="nav-item nav-link css-193va6t1" href="sources.html">Sources</a>

        </div>
      </div>
    </div>
  </nav>
</header>


"""
###############################################################################################################################################################################
bottom = """

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

</body>
</html>
 """

###############################################################################################################################################################################
add_content = """

    <!-- Add Content! -->
    <!-- Add Content! -->
    <!-- Add Content! -->
    <!-- Add Content! -->

"""
###############################################################################################################################################################################
home_content = """
<script>
        // Set the date we're counting down to
        var countDownDate = new Date("Nov 3, 2020 00:00:01").getTime();

        // Update the count down every 1 second
        var x = setInterval(function() {

          // Get today's date and time
          var now = new Date().getTime();

          // Find the distance between now and the count down date
          var distance = countDownDate - now;

          // Time calculations for days, hours, minutes and seconds
          var days = Math.floor(distance / (1000 * 60 * 60 * 24));


          // Display the result in the element with id="demo"
          document.getElementById("demo").innerHTML = days
          // If the count down is finished, write some text
          if (distance < 0) {
            clearInterval(x);
            document.getElementById("demo").innerHTML = "EXPIRED";
          }
        }, 1000);

</script>

    <main role="main" class="container">
    <main class="css-17j3c3d">
    <div class="row">
    <div class="col-md-8">
    <div class="css-zwkg4z">
    <div class=".css-89xpxa">


    <section style="position:relative">

    <!-- Top Story Header -->
    <header>
    <div class="css-18wsigh">
    <span class="css-x5e31x">
    <span class="css-1jr5l57"><b> News </b> </span> "Top Story" </span>
    </div>
    <br>
    </header>


    <!-- Top Story Picture -->
    <article>
    <a href="hack.html">
    <div>
    <img title="SC Top Story" width="90%" src="images/election_day.jpg">
    </img>
    </div>

    <!-- Top Story Description -->
    <h2 class="css-rlawu">
    Post Election Results
    </h2>
    <div>
    <span class="css-o3ula8 e13bwyn60">
    By
    <!-- -->
    Sean Williams
    </span>
    </div>
    </a>
    </article>






    </section>
    </div>
    </div>
    </div>



    <div class="col-md-4" style="position:relative">
    <section>



    <!-- Other Articles Header -->
    <header>
    <span class="css-x5e31x">
    <span class="css-1jr5l57"> <b> News </b>  </span> "Featured" </span>
    </header>



    <!-- Other Articles -->
    <div class="css-z78f2p">


    <article class="css-1tdvlph">

    <a class="css-k008qs" href="hack.html">
    <div class="css-1ev106r">
    <div class="css-8atqhb">
    <img title="Another Story" width="100%" src="images/CunninghamStory.jpg">
    </div>
    </div>

    <div class="css-hoe9xz">


      <h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
      Environmental laws passed by Cunningham
      </h3>

    <div class="css-94x4tq e13bwyn60">
    By <!-- --> Keelin White
    </div>

    </div>
    </a>

    </article>

    <article class="css-1tdvlph">
      <a class="css-k008qs" href="hack.html">
      <div class="css-1ev106r">
      <div class="css-8atqhb">
      <img title="Another Story" width="100%" src="images/Lindsey_Graham.jpg">
      </div>
      </div>

      <div class="css-hoe9xz">


        <h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
        Is it over for Graham?
        </h3>

      <div class="css-94x4tq e13bwyn60">
      By <!-- --> Sandra Black
      </div>

      </div>
      </a>

    </article>

    <article class="css-1tdvlph">
      <a class="css-k008qs" href="hack.html">
      <div class="css-1ev106r">
      <div class="css-8atqhb">
      <img title="Another Story" width="100%" src="images/Scott.jpeg">
      </div>
      </div>

      <div class="css-hoe9xz">


        <h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
        Is Tim Scott the future of the GOP?
        </h3>

      <div class="css-94x4tq e13bwyn60">
      By <!-- -->Joseph Curl
      </div>

      </div>
      </a>

    </article>


    </section>
    </div>



    </div>

    </main>
    </main>

    <div class="Toastify"><br><br></div>
    <div class="css-d7h9ck">
      <section id="election-signup" class="css-dhro7d e1kbyuqk0" width="100%">
        <h1 class="css-5w0168 e1kbyuqk1">
          <br>
          <span class="css-3ulb31 e17f3ixj1" id="demo">
          </span>

          <span class="css-1cbifvp e1kbyuqk2"> days <!-- -->until election</span>
        </h1>

        <div class="css-0 e1kbyuqk3">
        <h2 class="css-12xet20 e1kbyuqk4">Don't miss out on our coverage.</h2>
        <br> <br><br><br>
        </div>
    </div>


"""
###############################################################################################################################################################################

not_done_content = """
  <h1 align="middle"> We are hiring Politcal Journalist!!! </h1>
"""



###############################################################################################################################################################################
Candidates_content="""
<div class="container">
<div class="row">
<div class="col">
<h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
Incumbents
</h3>
<br>
<table class="table">
  <thead>
    <tr class="table-active">
      <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">House</th>
      <th scope="col">District</th>
      <th scope="col">Party</th>
      <th scope="col">Twitter</th>
      <th scope="col">Website</th>
    </tr>
  </thead>
  <tbody>


    <tr class="table-primary">
      <th scope="row">1</th>
      <td>Joe Cunningham</td>
      <td>House of Reps</td>
      <td>1</td>
      <td>Democrat</td>
      <td><a href="https://twitter.com/JoeCunninghamSC" target="_blank" class="css-k008qs">@JoeCunninghamSC</a></td>
      <td><a href="https://www.joecunninghamforcongress.com" target="_blank" class="css-k008qs">JoeCunninghamForCongress</a></td>
    </tr>

    <tr class="table-danger">
      <th scope="row">2</th>
      <td>Joe Wilson</td>
      <td>House of Reps</td>
      <td>2</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/RepJoeWilson" target="_blank" class="css-k008qs">@RepJoeWilson</a></td>
      <td><a href="https://joewilson.house.gov/" target="_blank" class="css-k008qs">JoeWilsonForCongress</a></td>
    </tr>

    <tr class="table-danger">
      <th scope="row">3</th>
      <td>Jeff Duncan</td>
      <td>House of Reps</td>
      <td>3</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/RepJeffDuncan" target="_blank" class="css-k008qs">@RepJeffDuncan</a></td>
      <td><a href="https://jeffduncan.house.gov/" target="_blank" class="css-k008qs">JeffDuncanForCongress</a></td>
    </tr>

    <tr class="table-danger">
      <th scope="row">4</th>
      <td>William Timmons</td>
      <td>House of Reps</td>
      <td>4</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/RepTimmons" target="_blank" class="css-k008qs">@RepTimmons</a></td>
      <td><a href="https://timmons.house.gov/" target="_blank" class="css-k008qs">WilliamTimmonsForCongress</a></td>
    </tr>

    <tr class="table-danger">
      <th scope="row">5</th>
      <td>Ralph Norman</td>
      <td>House of Reps</td>
      <td>5</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/RepRalphNorman" target="_blank" class="css-k008qs">@RepRalphNorman</a></td>
      <td><a href="https://norman.house.gov/" target="_blank" class="css-k008qs">RalphNormanForCongress</a></td>
    </tr>

    <tr class="table-primary">
      <th scope="row">6</th>
      <td>James Clyburn</td>
      <td>House of Reps</td>
      <td>6</td>
      <td>Democrat</td>
      <td><a href="https://twitter.com/ClyburnSC06" target="_blank" class="css-k008qs">@ClyburnSC06</a></td>
      <td><a href="https://clyburn.house.gov/" target="_blank" class="css-k008qs">JamesClyburnForCongress</a></td>
    </tr>

    <tr class="table-danger">
      <th scope="row">7</th>
      <td>Tom Rice</td>
      <td>House of Reps</td>
      <td>7</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/RepTomRice" target="_blank" class="css-k008qs">@RepTomRice</a></td>
      <td><a href="https://rice.house.gov/" target="_blank" class="css-k008qs">TomRiceForCongress</a></td>
    </tr>


  </tbody>
</table>
</div>
</div>


<br>
<div class="row">
<div class="col">
<h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
Incumbent competitors
</h3>
<br>
<table class="table">
  <thead>
    <tr>
           <th scope="col">#</th>
           <th scope="col">Name</th>
           <th scope="col">House</th>
           <th scope="col">District</th>
           <th scope="col">Party</th>
           <th scope="col">Twitter</th>
           <th scope="col">Website</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-danger">
      <th scope="row">1</th>
      <td>Nancy Mace</td>
      <td>House of Reps</td>
      <td>1</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/NancyMace?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" target="_blank" class="css-k008qs">@NancyMace</a></td>
      <td><a href="https://nancymace.org" target="_blank" class="css-k008qs"> NancyMaceForCongress </a><td>
    </tr>

    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Adair Boroughs</td>
      <td>House of Reps</td>
      <td>2</td>
      <td>Democrat</td>
      <td><a href="https://twitter.com/AdairFromSC" target="_blank" class="css-k008qs">@AdairFromSC</a></td>
      <td><a href="https://www.adairforcongress.com" target="_blank" class="css-k008qs"> AdairFromSC </a><td>
    </tr>

    <tr class="table-primary">
      <th scope="row">3</th>
      <td>Hosea Cleveland</td>
      <td>House of Reps</td>
      <td>3</td>
      <td>Democrat</td>
      <td><a href="https://twitter.com/ClevelandHosea" target="_blank" class="css-k008qs">@ClevelandHosea</a></td>
      <td><a href="https://www.adairforcongress.com" target="_blank" class="css-k008qs"> HoseaForCongress </a><td>
    </tr>

    <tr class="table-primary">
      <th scope="row">4</th>
      <td>Kim Nelson</td>
      <td>House of Reps</td>
      <td>4</td>
      <td>Democrat</td>
      <td><a href="https://twitter.com/KimforSC" target="_blank" class="css-k008qs">@kimforsc</a></td>
      <td><a href="https://www.kimnelsonforcongress.com" target="_blank" class="css-k008qs"> kimnelsonforcongress </a><td>
    </tr>

    <tr class="table-primary">
      <th scope="row">5</th>
      <td>John Mccollum</td>
      <td>House of Reps</td>
      <td>5</td>
      <td>Democrat</td>
      <td><a href="https://twitter.com/moebrownsc/" target="_blank" class="css-k008qs">@MoeBrownSC</a></td>
      <td><a href="https://www.moeforcongress.com/" target="_blank" class="css-k008qs"> Moeforcongress </a><td>
    </tr>

    <tr class="table-danger">
      <th scope="row">6</th>
      <td>John Mccollum</td>
      <td>House of Reps</td>
      <td>6</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/mccollumfor" target="_blank" class="css-k008qs">@Mccollumfor</a></td>
      <td><a href="https://www.johnforsc.com/" target="_blank" class="css-k008qs"> johnforsc </a><td>
    </tr>

    <tr class="table-primary">
      <th scope="row">7</th>
      <td>Melissa Watson</td>
      <td>House of Reps</td>
      <td>7</td>
      <td>Democrat</td>
      <td><a href="ttps://twitter.com/melissawatsonf1" target="_blank" class="css-k008qs">@melissawatsonf1</a></td>
      <td><a href="https://www.melissawatsonforcongress.com" target="_blank" class="css-k008qs"> melissawatsonforcongress </a><td>
    </tr>

  </tbody>
</table>
</div>
</div>
</div>

"""
###############################################################################################################################################################################

House_Results = """
<div class="container">
<div class="row">
<div class="col">
<h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
Winners
</h3>
<br>
<table class="table">
  <thead>
    <tr class="table-active">
      <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">Party</th>
      <th scope="col">District</th>
      <th scope="col">Percentage</th>
      <th scope="col">Votes</th>
      <th scope="col">Total Votes</th>

    </tr>
  </thead>
  <tbody>


    <tr class="table-danger">
      <th scope="row">1</th>
      <td>Nancy Mace</td>
      <td>Republican</td>
      <td>1</td>
      <td>50.6%</td>
      <td>216,042</td>
      <td>426,669</td>

    </tr>

    <tr class="table-danger">
      <th scope="row">2</th>
      <td>Joe Wilson</td>
      <td>Republican</td>
      <td>2</td>
      <td>55.7%</td>
      <td>202,715</td>
      <td>357,833</td>

    </tr>

    <tr class="table-danger">
      <th scope="row">3</th>
      <td>Jeff Duncan</td>
      <td>Republican</td>
      <td>3</td>
      <td>71.2%</td>
      <td>237,538</td>
      <td>333,416</td>

    </tr>

    <tr class="table-danger">
      <th scope="row">4</th>
      <td>William Timmons</td>
      <td>Republican</td>
      <td>4</td>
      <td>61.7%</td>
      <td>222,126</td>
      <td>355,149</td>

    </tr>

    <tr class="table-danger">
      <th scope="row">5</th>
      <td>Ralph Norman</td>
      <td>Republican</td>
      <td>5</td>
      <td>60.1%</td>
      <td>220,005</td>
      <td>286,735</td>

    </tr>

    <tr class="table-primary">
      <th scope="row">6</th>
      <td>James Clyburn</td>
      <td>Democrat</td>
      <td>6</td>
      <td>68.2%</td>
      <td>197,477</td>
      <td>286,735</td>

    </tr>

    <tr class="table-danger">
      <th scope="row">7</th>
      <td>Tom Rice</td>
      <td>Republican</td>
      <td>7</td>
      <td>61.8%</td>
      <td>224,993</td>
      <td>363,856</td>

    </tr>



  </tbody>
</table>
</div>
</div>
</div>



"""
###############################################################################################################################################################################

senate_content = """

<div class="container">
<div class="row">
<div class="col">
<h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
Results
</h3>
<br>
<table class="table">
  <thead>
    <tr class="table-active">
      <th scope="col">#</th>
      <th scope="col">Outcome</th>
      <th scope="col">Name</th>
      <th scope="col">Party</th>
      <th scope="col">Percentage</th>
      <th scope="col">Votes</th>


    </tr>
  </thead>
  <tbody>


    <tr class="table-danger">
      <th scope="row">1</th>
      <td>Winner</td>
      <td>Lindsey Graham</td>
      <td>Republican</td>
      <td>54.5%</td>
      <td>1,369,125</td>


    </tr>

    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Loser</td>
      <td>Jaime Harrison</td>
      <td>Democrat</td>
      <td>44.2%</td>
      <td>1,110,804</td>


    </tr>


  </tbody>
</table>
</div>
</div>
</div>




"""

###############################################################################################################################################################################
senate_candidates = """

<div class="container">
<div class="row">
<div class="col">
<h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
Race
</h3>
<br>
<table class="table">
  <thead>
    <tr class="table-active">
      <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">House</th>
      <th scope="col">Party</th>
      <th scope="col">Twitter</th>
      <th scope="col">Website</th>
      <th scope="col">Incumbent?</th>
    </tr>
  </thead>
  <tbody>


    <tr class="table-danger">
      <th scope="row">1</th>
      <td>Lindsey Graham</td>
      <td>Senate</td>
      <td>Republican</td>
      <td><a href="https://twitter.com/LindseyGrahamSC" target="_blank" class="css-k008qs">@LindseyGrahamSC</a></td>
      <td><a href="https://www.lgraham.senate.gov/public/"target="_blank" class="css-k008qs">LindseyGrahamSC</a></td>
      <td>YES</td>
    </tr>

    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Jaime Harrison</td>
      <td>Senate</td>
      <td>Democrat</td>
      <td><a href="https://twitter.com/harrisonjaime" target="_blank" class="css-k008qs">@HarrisonJaime</a></td>
      <td><a href="https://jaimeharrison.com/" target="_blank" class="css-k008qs">jaimeharrison</a></td>
      <td>NO</td>
    </tr>




  </tbody>
</table>
</div>
</div>


"""
###############################################################################################################################################################################

my_rep = """



<div class="container">
<div class="row">
<div class="col">
<h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
Location
</h3>
<br>
<table class="table">
  <thead>
    <tr class="table-active">
      <th scope="col">District</th>
      <th scope="col"></th>

    </tr>
  </thead>
  <tbody>


    <tr>
      <th scope="row"></th>
      <td>1</td>
      <td><iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
       src="https://www.govtrack.us/congress/members/embed/mapframe?state=sc&district=1"></iframe></td>
    </tr>

    <tr>
      <th scope="row"></th>
      <td>2</td>
      <td><iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
       src="https://www.govtrack.us/congress/members/embed/mapframe?state=sc&district=2"></iframe></td>
    </tr>

    <tr>
      <th scope="row"></th>
      <td>3</td>
      <td><iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
       src="https://www.govtrack.us/congress/members/embed/mapframe?state=sc&district=3"></iframe></td>
    </tr>

    <tr>
      <th scope="row"></th>
      <td>4</td>
      <td><iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
       src="https://www.govtrack.us/congress/members/embed/mapframe?state=sc&district=4"></iframe></td>
    </tr>

    <tr>
      <th scope="row"></th>
      <td>5</td>
      <td><iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
       src="https://www.govtrack.us/congress/members/embed/mapframe?state=sc&district=5"></iframe></td>
    </tr>

    <tr>
      <th scope="row"></th>
      <td>6</td>
      <td><iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
       src="https://www.govtrack.us/congress/members/embed/mapframe?state=sc&district=6"></iframe></td>
    </tr>

    <tr>
      <th scope="row"></th>
      <td>7</td>
      <td><iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
       src="https://www.govtrack.us/congress/members/embed/mapframe?state=sc&district=7"></iframe></td>
    </tr>




  </tbody>
</table>
</div>
</div>




"""

###############################################################################################################################################################################

sources = """

<div class="container">
<div class="row">
<div class="col">
<h3 style="color:#0D0D0D;margin-top:0" class="css-1628fxq e7f1hlv0">
Best Sources to keep up with the election and the congressional elects' term
</h3>
<br>
<table class="table">
  <thead>
    <tr class="table-active">
      <th scope="col">#</th>
      <th scope="col">Source</th>

    </tr>
  </thead>
  <tbody>


    <tr class="table-danger">
      <th scope="row">1</th>
      <td><a href="https://www.govtrack.us/" target="_blank" class="css-k008qs">GovTrack</a></td>
    </tr>


    <tr class="table-primary">
      <th scope="row">2</th>
      <td><a href="https://www.cnn.com" target="_blank" class="css-k008qs">CNN</a></td>
    </tr>

    <tr class="table-danger">
      <th scope="row">3</th>
      <td><a href="https://www.nytimes.com" target="_blank" class="css-k008qs">NYTimes</a></td>
    </tr>

    <tr class="table-primary">
      <th scope="row">4</th>
      <td><a href="https://apnews.com/" target="_blank" class="css-k008qs">AP NEWS</a></td>
    </tr>

    <tr class="table-danger">
      <th scope="row">5</th>
      <td><a href="https://www.pbs.org/newshour/" target="_blank" class="css-k008qs">PBS NEWS</a></td>
    </tr>

    <tr class="table-primary">
      <th scope="row">6</th>
      <td><a href="https://www.wsj.com" target="_blank" class="css-k008qs">Wall Street Journal</a></td>
    </tr>

    </tbody>



"""
