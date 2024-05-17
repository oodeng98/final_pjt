<template>
  <div>
    <h1>Map</h1>
    <div>
      <h2>Select Bank</h2>
      <div v-for="bank in banks" :key="bank">
        <input
          type="radio"
          :id="bank"
          name="bank"
          :value="bank"
          v-model="selectedBank"
        />
        <label :for="bank">{{ bank }}</label>
      </div>
    </div>
    <div>
      <h2>Select Region</h2>
      <div v-for="region in regions" :key="region">
        <input
          type="radio"
          :id="region"
          name="region"
          :value="region"
          v-model="selectedRegion"
        />
        <label :for="region">{{ region }}</label>
      </div>
    </div>
    <button @click="searchPlaces">Search</button>
    <div id="map" style="width: 500px; height: 400px"></div>
    <ul>
      <li v-for="place in places" :key="place.id">{{ place.place_name }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const banks = ref(["국민은행", "신한은행", "우리은행", "농협은행"]);
const regions = ref(["강남", "종로", "마포", "영등포"]);
const selectedBank = ref("");
const selectedRegion = ref("");
const places = ref([]);
let map;

const initializeMap = () => {
  const container = document.getElementById("map");
  const options = {
    center: new kakao.maps.LatLng(37.5665, 126.978), // 서울 중심 좌표
    level: 3,
  };
  map = new kakao.maps.Map(container, options);
};

const searchPlaces = () => {
  if (!selectedBank.value || !selectedRegion.value) {
    alert("Please select both a bank and a region!");
    return;
  }

  const query = `${selectedBank.value} ${selectedRegion.value}`;

  if (
    typeof kakao === "undefined" ||
    typeof kakao.maps === "undefined" ||
    typeof kakao.maps.services === "undefined"
  ) {
    console.error("Kakao Maps API is not loaded yet.");
    return;
  }

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(query, (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      places.value = data;
      displayPlaces(data);
    } else {
      alert("Search failed!");
    }
  });
};

const displayPlaces = (places) => {
  const bounds = new kakao.maps.LatLngBounds();
  for (let i = 0; i < places.length; i++) {
    const place = places[i];
    const markerPosition = new kakao.maps.LatLng(place.y, place.x);
    const marker = new kakao.maps.Marker({
      position: markerPosition,
    });
    marker.setMap(map);
    bounds.extend(markerPosition);
  }
  map.setBounds(bounds);
};

onMounted(() => {
  if (typeof kakao !== "undefined" && kakao.maps) {
    initializeMap();
  } else {
    console.error("Kakao Maps API failed to load.");
  }
});
</script>

<style scoped>
#map {
  width: 500px;
  height: 400px;
}
</style>
