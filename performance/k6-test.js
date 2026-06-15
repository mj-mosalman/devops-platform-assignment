import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 50,
  duration: "30s",
};

export default function () {

  let writeRes = http.post(
    "http://localhost:8010/write/load_key?value=performance"
  );

  check(writeRes, {
    "write status 200": (r) => r.status === 200,
  });

  let readRes = http.get(
    "http://localhost:8010/read/load_key"
  );

  check(readRes, {
    "read status 200": (r) => r.status === 200,
  });

  sleep(1);
}
