$flavor = $('#flavor');
$size = $('#size');
$rating = $('#rating');
$image = $('#image');
$cupcakeList = $("#getcupcakes");
$list = $("#list");
$create = $("#create");

$(document).ready(function() {
  $("#getcupcakes").click(getCupcakes);
});

async function getCupcakes() {
  const response = await axios.get("/api/cupcakes");
  const cupcakes = response.data.cupcakes;

  $list.empty(); // Clear the existing list

  cupcakes.forEach(cupcake => {
    $("<li>").text(cupcake.flavor).appendTo($list);
  });
}

$(document).ready(function() {
  $create.click(addCupcake);
});

async function addCupcake() {
  const data = {
    flavor: $flavor.val(),
    size: $size.val(),
    rating: $rating.val(),
    image: $image.val()
  };

  try {
    const response = await axios.post('/api/cupcakes', JSON.stringify(data), {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    console.log(response.data); // Handle the response data
  } catch (error) {
    console.error(error); // Handle any errors
  }
}
