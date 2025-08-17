function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("GitHub Actions"));
console.log(greet("Node CI updated!"));

module.exports = greet; // export for testing
