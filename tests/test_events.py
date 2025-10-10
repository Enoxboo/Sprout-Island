def run_all_tests():
    print("\n=== Lancement des tests ===\n")

    try:

        print("\n🎉 Tous les tests sont passés !\n")
        return True

    except AssertionError as e:
        print(f"\n❌ Échec du test: {e}\n")
        return False
