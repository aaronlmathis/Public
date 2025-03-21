// Helper function to check if key exists in a map.
func inMap[K comparable, V any](m map[K]V, key K) bool {
	_, ok := m[key]
	return ok
}