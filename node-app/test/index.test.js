const greet = require("../index");

test("greets the user", () => {
    expect(greet("GitHub Actions")).toBe("Hello, GitHub Actions!");
});
