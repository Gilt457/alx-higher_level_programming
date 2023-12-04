#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the reversed list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *curr = *head, *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
}

/**
 * check_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int check_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *temp = *head, *rev = NULL;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	rev = slow;
	reverse_list(&rev);

	while (rev && temp)
	{
		if (rev->n != temp->n)
			return (0);
		rev = rev->next;
		temp = temp->next;
	}
	return (1);
}
